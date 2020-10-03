import pocketsmith


class PocketsmithClient:
    def __init__(self, api_key: str):
        configuration = pocketsmith.Configuration()
        configuration.api_key['X-Developer-Key'] = api_key
        self.api_client = pocketsmith.ApiClient(configuration)

        self.accounts = pocketsmith.AccountsApi(self.api_client)
        self.budgeting = pocketsmith.BudgetingApi(self.api_client)
        self.categories = pocketsmith.CategoriesApi(self.api_client)
        self.institutions = pocketsmith.InstitutionsApi(self.api_client)
        self.transaction_accounts = pocketsmith.TransactionAccountsApi(self.api_client)
        self.transactions = pocketsmith.TransactionsApi(self.api_client)
        self.users = pocketsmith.UsersApi(self.api_client)
