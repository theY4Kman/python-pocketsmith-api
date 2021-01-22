def it_imports():
    try:
        import pocketsmith
    except Exception as e:
        raise AssertionError(f'Encountered error importing library: {e}')


def it_makes_request():
    import pocketsmith
    client = pocketsmith.PocketsmithClient('dummy-api-key')

    try:
        client.users.get_me()
    except pocketsmith.ApiException:
        pass
    except Exception as e:
        raise AssertionError(f'Encountered error making request: {e}')
