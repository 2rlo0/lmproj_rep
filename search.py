import meilisearch
client = meilisearch.Client('http://127.0.0.1:7700/','fv1vhvklIFuav-3N9ynvG_OUhPOahBb8HQVItCEwIng')

def stock_search(query):
    return client.index('nasdaq').search(query)