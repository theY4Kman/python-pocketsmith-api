from typing import Optional

import certifi
import pocketsmith

__all__ = ['PocketsmithClient']


class PocketsmithClient:
    def __init__(
        self, api_key: str, *,
        ssl_ca_cert: Optional[str] = certifi.where(),
        **settings,
    ):
        configuration = pocketsmith.Configuration(
            api_key={'developerKey': api_key},
            ssl_ca_cert=ssl_ca_cert,
            **settings,
        )
        self.api_client = pocketsmith.ApiClient(configuration)

        self.accounts = pocketsmith.AccountsApi(self.api_client)
        self.attachments = pocketsmith.AttachmentsApi(self.api_client)
        self.budgeting = pocketsmith.BudgetingApi(self.api_client)
        self.categories = pocketsmith.CategoriesApi(self.api_client)
        self.category_rules = pocketsmith.CategoryRulesApi(self.api_client)
        self.data_feeds_accounts = pocketsmith.DataFeedsAccountsApi(self.api_client)
        self.data_feeds_connections = pocketsmith.DataFeedsConnectionsApi(self.api_client)
        self.institutions = pocketsmith.InstitutionsApi(self.api_client)
        self.transaction_accounts = pocketsmith.TransactionAccountsApi(self.api_client)
        self.transactions = pocketsmith.TransactionsApi(self.api_client)
        self.users = pocketsmith.UsersApi(self.api_client)
