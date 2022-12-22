import environ

env = environ.Env()
environ.Env.read_env()

THREEKIT_BEARER_TOKEN = env('THREEKIT_BEARER_TOKEN')
THREEKIT_ORG_ID = env('THREEKIT_ORG_ID')
THREEKIT_HOST = env('THREEKIT_HOST')

FROM_COMPOSITE = env('FROM_COMPOSITE')
TO_COMPOSITE = env('TO_COMPOSITE')
