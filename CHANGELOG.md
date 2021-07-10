# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/)
and this project adheres to [Semantic Versioning](http://semver.org/spec/v2.0.0.html).


## [Unreleased]
### Added
 - Added missing `currency_code` field to `BudgetAnalysis` and `Period` types (see [GH#6](https://github.com/theY4Kman/python-pocketsmith-api/pull/6), thanks [@brett-comber](https://github.com/brett-comber))

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
