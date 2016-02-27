'use strict';

require('dotenv').load();

const request = require('request-promise');
const _ = require('lodash');
const moment = require('moment');
const json2csv = require('json2csv');
const fs = require('fs');

function daysOnMarket(listing) {
  let days_on_market = moment().diff(listing.created_date, 'days');
  if (listing.removed_date) {
    days_on_market = moment(listing.removed_date).diff(listing.created_date, 'days');
  }

  return days_on_market;
}

function cleanListings(listings) {
  return JSON.parse(listings).map(processListing);
}

function processListing(listing) {
  const amounts = _.sortBy(listing.listingAmounts, 'created_date');
  const start_price = amounts[0].listing_amount;
  const current_price = amounts[amounts.length - 1].listing_amount;
  const num_price_adjustments = amounts.length;
  const sold = listing.removed_date ? 1 : 0;
  const percent_change_price = (current_price - start_price) / start_price;
  const days_on_market = daysOnMarket(listing);

  const re = /([0-9])\w+/;
  const size_interior = listing.size_interior ? re.exec(listing.size_interior)[0] : 0;

  return Object.assign({}, listing, {
    num_bathrooms: eval(listing.num_bathrooms) || 0, // trust me, i know what i'm doing...
    num_bedrooms: eval(listing.num_bedrooms) || 0,
    sold,
    size_interior: parseInt(size_interior, 10),
    days_on_market,
    num_price_adjustments,
    percent_change_price,
    start_price: parseFloat(start_price),
    current_price: parseFloat(current_price),
    description: listing.public_remarks
  });
}

function convertToCSV(data) {
  const fields = [
    'mls_number',
    'description',
    'num_bathrooms',
    'num_bedrooms',
    'building_type',
    'size_interior',
    'latitude',
    'longitude',
    'ownership_type',
    'sold',
    'days_on_market',
    'num_price_adjustments',
    'percent_change_price',
    'start_price',
    'current_price'
  ];

  return new Promise((resolve, reject) => {
    json2csv({data, fields}, (err, csv) => {
      if (err) {
        reject(err);
      } else {
        resolve(csv);
      }
    });
  });
}

function outputCSVFile(filename) {
  return csv => new Promise((resolve, reject) => {
    fs.writeFile(filename, csv, err => {
      if (err) {
        reject(err);
      } else {
        resolve('Wrote file ' + filename);
      }
    });
  });
}

request(`${process.env.MOONRAKER_API_URL}/api/listings/`)
  .then(cleanListings)
  .then(convertToCSV)
  .then(outputCSVFile('listings.csv'))
  .then(console.log);
