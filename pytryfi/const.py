SENTRY_URL = "https://c7618923f758480ca2af05a21123f855@o580516.ingest.sentry.io/5735605"

PYTRYFI_VERSION = "0.0.19"

API_HOST_URL_BASE = "https://api.tryfi.com"
API_GRAPHQL = "/graphql"
API_LOGIN = "/auth/login"

PET_MODE_NORMAL = "NORMAL"
PET_MODE_LOST = "LOST_DOG"
PET_ACTIVITY_ONGOINGWALK = "OngoingWalk"
PET_ACTIVITY_ONGOINGREST = "OngoingRest"
PET_ACTIVITY_WALK = "Walk"
PET_ACTIVITY_REST = "Rest"

VAR_PET_ID = "__PET_ID__"

QUERY_CURRENT_USER = "query {\n  currentUser {\n    ...UserDetails\n  }\n}\n"
QUERY_CURRENT_USER_FULL_DETAIL = (
    "query {\n  currentUser {\n    ...UserFullDetails\n  }\n}\n"
)
QUERY_PET_CURRENT_LOCATION = (
    'query {\n\n  pet (id: "'
    + VAR_PET_ID
    + '") {\n    ongoingActivity {\n      __typename\n      ...OngoingActivityDetails\n    }\n  }\n}\n'
)
QUERY_PET_ACTIVITY = (
    'query {\n\n  pet (id: "'
    + VAR_PET_ID
    + '") {\n   \n    dailyStat: currentActivitySummary (period: DAILY) {\n      ...ActivitySummaryDetails\n    }\n    weeklyStat: currentActivitySummary (period: WEEKLY) {\n      ...ActivitySummaryDetails\n    }\n    monthlyStat: currentActivitySummary (period: MONTHLY) {\n      ...ActivitySummaryDetails\n    }\n  }\n}\n'
)
QUERY_PET_REST = (
    'query {\n  pet (id: "'
    + VAR_PET_ID
    + '") {\n	dailyStat: restSummaryFeed(cursor: null, period: DAILY, limit: 1) {\n      __typename\n      restSummaries {\n        __typename\n        ...RestSummaryDetails\n      }\n    }\n	weeklyStat: restSummaryFeed(cursor: null, period: WEEKLY, limit: 1) {\n      __typename\n      restSummaries {\n        __typename\n        ...RestSummaryDetails\n      }\n    }\n	monthlyStat: restSummaryFeed(cursor: null, period: MONTHLY, limit: 1) {\n      __typename\n      restSummaries {\n        __typename\n        ...RestSummaryDetails\n      }\n    }\n  }\n}'
)
QUERY_PET_DEVICE_DETAILS = (
    'query {\n  pet (id: "'
    + VAR_PET_ID
    + '") {\n    __typename\n    ...PetProfile\n  }\n}\n'
)

FRAGMENT_USER_DETAILS = "fragment UserDetails on User {\n  __typename\n   id\n  email\n  firstName\n  lastName\n  phoneNumber\n  fiNewsNotificationsEnabled\n  chipReseller {\n    __typename\n    id\n  }\n}\n"
FRAGMENT_USER_FULL_DETAILS = "fragment UserFullDetails on User {\n  __typename\n  ...UserDetails\n  userHouseholds {\n    __typename\n    household {\n      __typename\n      pets {\n        __typename\n        ...PetProfile\n      }\n      bases {\n        __typename\n        ...BaseDetails\n      }\n    }\n  }\n}\n"
FRAGEMENT_BASE_PET_PROFILE = "fragment BasePetProfile on BasePet {\n  __typename\n  id\n  name\n  homeCityState\n  yearOfBirth\n  monthOfBirth\n  dayOfBirth\n  gender\n  weight\n  isPurebred\n  breed {\n    __typename\n    ...BreedDetails\n  }\n  photos {\n    __typename\n    first {\n      __typename\n      ...PhotoDetails\n    }\n    items {\n      __typename\n      ...PhotoDetails\n    }\n  }\n  instagramHandle\n  \n}\n"
FRAGMENT_BREED_DETAILS = "fragment BreedDetails on Breed {\n  __typename\n  id\n  name\n  popularityScore\n}\n"
FRAGMENT_PHOTO_DETAILS = "fragment PhotoDetails on Photo {\n  __typename\n  id\n  caption\n  date\n  likeCount\n  liked\n  image {\n    __typename\n    fullSize\n  }\n}\n"
FRAGMENT_PET_PROFILE = "fragment PetProfile on Pet {\n  __typename\n  ...BasePetProfile\n  chip {\n    __typename\n    shortId\n  }\n  device {\n    __typename\n    ...DeviceDetails\n  }\n}\n"
FRAGMENT_DEVICE_DETAILS = "fragment DeviceDetails on Device {\n  __typename\n  id\n  moduleId\n  info\n  subscriptionId\n  hasActiveSubscription\n  hasSubscriptionOverride\n  nextLocationUpdateExpectedBy\n  operationParams {\n    __typename\n    ...OperationParamsDetails\n  }\n  lastConnectionState {\n    __typename\n    ...ConnectionStateDetails\n  }\n  ledColor {\n    __typename\n    ...LedColorDetails\n  }\n  availableLedColors {\n    __typename\n    ...LedColorDetails\n  }\n}\n"
FRAGMENT_LED_DETAILS = "fragment LedColorDetails on LedColor {\n  __typename\n  ledColorCode\n  hexCode\n  name\n}\n"
FRAGMENT_CONNECTION_STATE_DETAILS = "fragment ConnectionStateDetails on ConnectionState {\n  __typename\n  date\n  ... on ConnectedToUser {\n    user {\n      __typename\n      ...UserDetails\n    }\n  }\n  ... on ConnectedToBase {\n    chargingBase {\n      __typename\n      id\n    }\n  }\n  ... on ConnectedToCellular {\n    signalStrengthPercent\n  }\n  ... on UnknownConnectivity {\n    unknownConnectivity\n  }\n}\n"
FRAGMENT_OPERATIONAL_DETAILS = "fragment OperationParamsDetails on OperationParams {\n  __typename\n  mode\n  ledEnabled\n  ledOffAt\n}\n"
FRAGMENT_BASE_DETAILS = "fragment BaseDetails on ChargingBase {\n  __typename\n  baseId\n  name\n  position {\n    __typename\n    ...PositionCoordinates\n  }\n  infoLastUpdated\n  networkName\n  online\n  onlineQuality\n}\n"
FRAGMENT_POSITION_COORDINATES = "fragment PositionCoordinates on Position {\n  __typename\n  latitude\n  longitude\n}\n"
FRAGMENT_ONGOING_ACTIVITY_DETAILS = "fragment OngoingActivityDetails on OngoingActivity {\n  __typename\n  start\n  presentUser {\n    __typename\n    ...UserDetails\n  }\n  areaName\n  lastReportTimestamp\n  obfuscatedReason\n  totalSteps\n  uncertaintyInfo {\n    __typename\n    ...UncertaintyInfoDetails\n  }\n  ... on OngoingWalk {\n    distance\n    positions {\n      __typename\n      ...LocationPoint\n    }\n    path {\n      __typename\n      ...PositionCoordinates\n    }\n  }\n  ... on OngoingRest {\n    position {\n      __typename\n      ...PositionCoordinates\n    }\n    place {\n      __typename\n      ...PlaceDetails\n    }\n  }\n}\n"
FRAGMENT_UNCERTAINTY_DETAILS = "fragment UncertaintyInfoDetails on UncertaintyInfo {\n  __typename\n  areaName\n  updatedAt\n  circle {\n    __typename\n    ...CircleDetails\n  }\n}\n"
FRAGMENT_CIRCLE_DETAILS = "fragment CircleDetails on Circle {\n  __typename\n  radius\n  latitude\n  longitude\n}\n"
FRAGMENT_LOCATION_POINT = "fragment LocationPoint on Location {\n  __typename\n  date\n  errorRadius\n  position {\n    __typename\n    ...PositionCoordinates\n  }\n}\n"
FRAGMENT_PLACE_DETAILS = "fragment PlaceDetails on Place {\n  __typename\n  id\n  name\n  address\n  position {\n    __typename\n    ...PositionCoordinates\n  }\n  radius\n}\n"
FRAGMENT_ACTIVITY_SUMMARY_DETAILS = "fragment ActivitySummaryDetails on ActivitySummary {\n  __typename\n  start\n  end\n  totalSteps\n  stepGoal\n  dailySteps {\n    __typename\n    date\n    totalSteps\n    stepGoal\n  }\n  totalDistance\n}\n"
FRAGMENT_REST_SUMMARY_DETAILS = "fragment RestSummaryDetails on RestSummary {\n  __typename\n  start\n  end\n  data {\n    __typename\n    ... on ConcreteRestSummaryData {\n      sleepAmounts {\n        __typename\n        type\n        duration\n      }\n    }\n  }\n}\n"
MUTATION_DEVICE_OPS = "mutation UpdateDeviceOperationParams($input: UpdateDeviceOperationParamsInput!) {\n  updateDeviceOperationParams(input: $input) {\n    __typename\n    ...DeviceDetails\n  }\n}\n"
MUTATION_SET_LED_COLOR = "mutation SetDeviceLed($moduleId: String!, $ledColorCode: Int!) {\n  setDeviceLed(moduleId: $moduleId, ledColorCode: $ledColorCode) {\n    __typename\n    ...DeviceDetails\n  }\n}\n"
