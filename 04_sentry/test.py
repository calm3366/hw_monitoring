import sentry_sdk

sentry_sdk.init(
    dsn="https://6507fd361b3f8bea5bc36b569978607c@o4506631040729088.ingest.sentry.io/4506631049052160",
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    traces_sample_rate=1.0,
    # Set profiles_sample_rate to 1.0 to profile 100%
    # of sampled transactions.
    # We recommend adjusting this value in production.
    profiles_sample_rate=1.0,
)

division_by_zero = 1 / 0