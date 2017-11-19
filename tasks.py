from invoke import Collection
from invocations.docs import docs


ns = Collection(docs)
ns.configure({
    'sphinx': {
        'source': 'source',
        'target': 'build',
        'target_file': 'index.html'
    }
})
