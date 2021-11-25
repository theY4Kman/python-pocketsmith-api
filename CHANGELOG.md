# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/)
and this project adheres to [Semantic Versioning](http://semver.org/spec/v2.0.0.html).


## [Unreleased]


## [2.1.0] — 2021-11-25
### Added
 - Allow additional PocketSmith client configuration to be specified during instantiation

### Fixed
 - Resolve SSL cert validation error due to lack of CA cert bundle in urllib3 client
 - Fix type validation errors due to Data Feeds schemas expecting ints but getting strings


## [2.0.3] — 2021-11-22
### Fixed
 - Restore previously-used import paths (whoops!)


## [2.0.2] — 2021-11-22
### Changed
 - Upgrade openapi-generator to 5.3.0 (previously using ancient 4.3.1)

### Fixed
 - Resolve some validation errors with Data Feeds Connections


## [2.0.1] — 2021-11-22
### Fixed
 - Avoid validation errors with tentative Data Feeds enums when PocketSmith returns an undeclared value


## [2.0.0] — 2021-11-21
### Breaking
 - Renamed Data Connections to Data Feeds Connections (now `DataFeedsConnectionsApi`, exposed as `PocketsmithClient.data_feeds_connections`)

### Added
 - Added Data Feeds Accounts (see `DataFeedsAccountsApi`, exposed as `PocketsmithClient.data_feeds_accounts`)
 - Added missing Data Feeds related fields to Transaction Accounts (`data_feeds_account_id`, `data_feeds_balance_type`, and `data_feeds_connection_id`)


## [1.3.0] — 2021-11-10
### Added
 - Added tentative Data Connections support (see `DataConnectionsApi`, exposed as `PocketsmithClient.data_connections`)


## [1.2.0] — 2021-07-10
### Added
 - Added missing `currency_code` field to `BudgetAnalysis` and `Period` types (see [GH#6](https://github.com/theY4Kman/python-pocketsmith-api/pull/6), thanks [@brett-comber](https://github.com/brett-comber))

### Changed
 - User-Agent reported by client changed to `python-pocketsmith/<version>` (previously was `OpenAPI-Generator/<version>/python`)

### Fixed
 - `budgeting.get_trend_analysis()` now returns proper response data (see [GH#6](https://github.com/theY4Kman/python-pocketsmith-api/pull/6), thanks [@brett-comber](https://github.com/brett-comber))
 - Corrected typo in `refund_amount`, was previously `refund_amound` (see [GH#6](https://github.com/theY4Kman/python-pocketsmith-api/pull/6), thanks [@brett-comber](https://github.com/brett-comber))
 - `__version__` now correctly reported from `pocketsmith` package (see [GH#6](https://github.com/theY4Kman/python-pocketsmith-api/pull/6), thanks [@brett-comber](https://github.com/brett-comber))


## [1.1.0] — 2021-07-08
### Added
 - Expose overlooked `attachments` and `category_rules` API clients on `PocketsmithClient` (see [GH#4](https://github.com/theY4Kman/python-pocketsmith-api/pull/4), thanks [@brett-comber](https://github.com/brett-comber))


## [1.0.1] — 2021-01-22
### Fixed
 - Include required `certifi` dependency when installing


## [1.0.0] — 2020-10-12
### Changed
 - Remove support for Python 2.7 — support only given for 3.6+


## [0.1.0] — 2020-10-03
### Added
 - Initial release: auto-generated OpenAPI client, with curated Pocketsmith API Client class
