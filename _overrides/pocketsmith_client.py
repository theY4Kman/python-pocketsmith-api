import pocketsmith
import pocketsmith.apis


class PocketsmithClient:
    def __init__(self, api_key: str):
        configuration = pocketsmith.Configuration(api_key={'developerKey': api_key})
        self.api_client = pocketsmith.ApiClient(configuration)

        self.accounts = pocketsmith.apis.AccountsApi(self.api_client)
        self.attachments = pocketsmith.apis.AttachmentsApi(self.api_client)
        self.budgeting = pocketsmith.apis.BudgetingApi(self.api_client)
        self.categories = pocketsmith.apis.CategoriesApi(self.api_client)
        self.category_rules = pocketsmith.apis.CategoryRulesApi(self.api_client)
        self.data_feeds_accounts = pocketsmith.apis.DataFeedsAccountsApi(self.api_client)
        self.data_feeds_connections = pocketsmith.apis.DataFeedsConnectionsApi(self.api_client)
        self.institutions = pocketsmith.apis.InstitutionsApi(self.api_client)
        self.transaction_accounts = pocketsmith.apis.TransactionAccountsApi(self.api_client)
        self.transactions = pocketsmith.apis.TransactionsApi(self.api_client)
        self.users = pocketsmith.apis.UsersApi(self.api_client)
