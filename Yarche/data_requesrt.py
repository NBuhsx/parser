###Я ебал в рот этого разработчика

from typing import Union







def data_for_get_coordinat(adress:str):
    return  {
            "query":"\n  query($input: SearchByAddressInput!) {\n    geocode: searchByAddress(input: $input) {\n      \n  text\n  kind\n  precision\n  lat\n  long\n\n    }\n  }\n",
            "variables": "{\"input\":{\"search\":\"" + adress + " \"}}"}


def data_for_set_adress(adress:str, coordinats:tuple):
    return {
            "query": "\n  mutation ($input: SetCurrentAddressRequest!) {\n    setCurrentAddress (input: $input) {\n      \n  id\n  status\n  title\n  address\n  porch\n  floor\n  flat\n  firstname\n  lastname\n  phone\n  isDefault\n  isAccurate\n  coordinates {\n  latitude\n  longitude\n}\n  comment\n  stocks {\n  id\n  name\n  description\n  vendorGuid\n}\n  isDraft\n  isPrivateHouse\n\n    }\n  }\n",
            "variables": "{\"input\":{\"address\":\"" + adress + "\",\"coordinates\":{\"latitude\":" + 
                    str(coordinats[0]) + ",\"longitude\":" + 
                    str(coordinats[1]) + "},\"isAccurate\":true}}"}



def data_for_get_category():
    return {"query":"\n  query (\n  $productsNewestSort: SortInput, \n  $productsNewestPagination: PageInput, \n  $productsBestsellerSort: SortInput, \n  $productsBestsellerPagination: \
PageInput, \n  $metaTagsFilter: [String], \n  $staticContentFilter: [String]!\n) {\n    \n  categories {\n  \n  id\n  name\n  code\n  treeId\n  parentTreeId\n\n  description\n  amount\n  \
image {\n  id\n  title\n  alt\n}\n  metaTags {\n  key\n  value\n}\n  isBold\n}\n  defaultCart {\n  id\n  name\n  products {\n  id\n  code\n  name\n  description\n  amount\n  \
image {\n  id\n  title\n  alt\n}\n  price\n  previousPrice\n  itemSum\n  isNew\n  isHit\n  isVkusvill\n  isFavorite\n  isAvailable\n  isSubscribed\n  isVeterinaryControl\n  quant \
{\n  code\n  fullName\n  shortName\n  multiple\n  pricePerUnit\n  previousPricePerUnit\n  unit\n  type\n  minAmount\n  stepAmount\n  currency\n}\n  categories {\n  id\n  name\n  code\n  \
treeId\n  parentTreeId\n}\n  rating\n  numberOfRatings\n}\n}\n  cartGroups {\n  id\n  products {\n  id\n  code\n  name\n  description\n  amount\n  image {\n  id\n  title\n  alt\n}\n  \
price\n  previousPrice\n  itemSum\n  isNew\n  isHit\n  isVkusvill\n  isFavorite\n  isAvailable\n  isSubscribed\n  isVeterinaryControl\n  quant {\n  code\n  fullName\n  shortName\n  \
multiple\n  pricePerUnit\n  previousPricePerUnit\n  unit\n  type\n  minAmount\n  stepAmount\n  currency\n}\n  categories {\n  id\n  name\n  code\n  treeId\n  parentTreeId\n}\n  \
rating\n  numberOfRatings\n}\n  agreement {\n  id\n  number\n  activeFrom\n  activeTo\n  minimalOrderSum\n  currency\n  agreementGroup {\n  code\n  name\n  isDefault\n  \
deliveryPersonGroupId\n}\n}\n  stock {\n    id\n  }\n  deliveryMethods {\n  code\n  title\n  description\n  isActive\n  priority\n  minDeliveryTime\n  maxDeliveryTime\n}\n  \
paymentMethods {\n  \n  code\n  title\n  description\n  isActive\n  dates\n  change {\n  code\n  value\n  currencyCode\n}\n\n  replacementMethods {\n  code\n  title\n}\n}\n}\n  metaTags \
(filter: $metaTagsFilter) {\n  key\n  value\n}\n  staticContent (filter: $staticContentFilter) {\n  key\n  value\n}\n  productsNewest (sort: $productsNewestSort, page: \
$productsNewestPagination) {\n    list {\n  id\n  code\n  name\n  description\n  amount\n  image {\n  id\n  title\n  alt\n}\n  price\n  previousPrice\n  itemSum\n  isNew\n  isHit\n  \
isVkusvill\n  isFavorite\n  isAvailable\n  isSubscribed\n  isVeterinaryControl\n  quant {\n  code\n  fullName\n  shortName\n  multiple\n  pricePerUnit\n  previousPricePerUnit\n  unit\n  \
type\n  minAmount\n  stepAmount\n  currency\n}\n  categories {\n  id\n  name\n  code\n  treeId\n  parentTreeId\n}\n  rating\n  numberOfRatings\n}\n    sort {\n  param\n  title\n  \
direct\n  isApplied\n}\n    page {\n  total\n  limit\n  page\n}\n  }\n  productsBestseller (sort: $productsBestsellerSort, page: $productsBestsellerPagination) {\n    list {\n  id\n  \
code\n  name\n  description\n  amount\n  image {\n  id\n  title\n  alt\n}\n  price\n  previousPrice\n  itemSum\n  isNew\n  isHit\n  isVkusvill\n  isFavorite\n  isAvailable\n  \
isSubscribed\n  isVeterinaryControl\n  quant {\n  code\n  fullName\n  shortName\n  multiple\n  pricePerUnit\n  previousPricePerUnit\n  unit\n  type\n  minAmount\n  stepAmount\n  \
currency\n}\n  categories {\n  id\n  name\n  code\n  treeId\n  parentTreeId\n}\n  rating\n  numberOfRatings\n}\n    sort {\n  param\n  title\n  direct\n  isApplied\n}\n    page \
{\n  total\n  limit\n  page\n}\n  }\n  banners {\n  title\n  alt\n  imageId\n  mobileImageId\n  link\n  isNewTab\n}\n  agreements {\n  id\n  number\n  activeFrom\n  activeTo\n  \
minimalOrderSum\n  currency\n  agreementGroup {\n  code\n  name\n  isDefault\n  deliveryPersonGroupId\n}\n}\n  profile {\n  id\n  lastname\n  firstname\n  email\n  phone\n  subscribe\n  \
isEmailVerified\n  isPhoneVerified\n  isRegistered\n  emailSignature\n  contractor {\n  # id\n  name\n  status\n  type\n  isActive\n  isVeterinaryApprove\n  requisiteData {\n  \
organizationName\n  address\n\n  ... on RequisiteRuIndividual {\n    inn\n  }\n\n  ... on RequisiteRuLegal {\n    inn\n    kpp\n  }\n\n  ... on RequisiteKz {\n    bin\n  }\n}\n  \
paymentMethods {\n  code\n  title\n  description\n  isActive\n  dates\n  change {\n  code\n  value\n  currencyCode\n}\n}\n}\n}\n  notifications (input: { platform: web }) {\n    \
list {\n      \n  id\n  message\n  secondToStart\n  secondToFinish\n\n    }\n  }\n  awaitingPaymentOrders: orders (filter: { status: awaiting_payment }) {\n    page {\n      total\n    \
}\n  }\n  mainPagePersonalRecommendations: recommendations (input: { type: personal, page: { page: 1, limit: 12 } }) {\n    list {\n  id\n  code\n  name\n  description\n  amount\n  image {\n  id\n  title\n  alt\n}\n  price\n  previousPrice\n  itemSum\n  isNew\n  isHit\n  isVkusvill\n  isFavorite\n  isAvailable\n  isSubscribed\n  isVeterinaryControl\n  quant {\n  code\n  fullName\n  shortName\n  multiple\n  pricePerUnit\n  previousPricePerUnit\n  unit\n  type\n  minAmount\n  stepAmount\n  currency\n}\n  categories {\n  id\n  name\n  code\n  treeId\n  parentTreeId\n}\n  rating\n  numberOfRatings\n}\n    page {\n  total\n  limit\n  page\n}\n  }\n  mainPageBoughtBeforeRecommendations: productsPreviouslyBought (input: { page: { page: 1, limit: 12 } }) {\n    list {\n  id\n  code\n  name\n  description\n  amount\n  image {\n  id\n  title\n  alt\n}\n  price\n  previousPrice\n  itemSum\n  isNew\n  isHit\n  isVkusvill\n  isFavorite\n  isAvailable\n  isSubscribed\n  isVeterinaryControl\n  quant {\n  code\n  fullName\n  shortName\n  multiple\n  pricePerUnit\n  previousPricePerUnit\n  unit\n  type\n  minAmount\n  stepAmount\n  currency\n}\n  categories {\n  id\n  name\n  code\n  treeId\n  parentTreeId\n}\n  rating\n  numberOfRatings\n}\n    page {\n  total\n  limit\n  page\n}\n  }\n  stocks {\n  id\n  name\n  description\n  vendorGuid\n}\n  currentAddress {\n  id\n  status\n  title\n  address\n  porch\n  floor\n  flat\n  firstname\n  lastname\n  phone\n  isDefault\n  isAccurate\n  coordinates {\n  latitude\n  longitude\n}\n  comment\n  stocks {\n  id\n  name\n  description\n  vendorGuid\n}\n  isDraft\n  isPrivateHouse\n}\n  confirmationDeliveryAddresses: deliveryAddresses (filter: { isDraft: false }, page: { page: 1, limit: 100 }) {\n    list {\n  id\n  status\n  title\n  address\n  porch\n  floor\n  flat\n  firstname\n  lastname\n  phone\n  isDefault\n  isAccurate\n  coordinates {\n  latitude\n  longitude\n}\n  comment\n  stocks {\n  id\n  name\n  description\n  vendorGuid\n}\n  isDraft\n  isPrivateHouse\n}\n    page {\n  total\n  limit\n  page\n}\n  }\n  locales {\n  locale\n  isDefault\n  isCurrent\n}\n  settings (filter: [\"contractor_enabled\",\"price_precision\",\"user\",\"order\",\"invoice\"]) {\n    \n  key\n  value\n\n  }\n  authentications {\n    \n  provider\n\n  }\n\n  }\n","variables":"{\"productsNewestPagination\":{\"page\":1,\"limit\":6},\"staticContentFilter\":[\"about\",\"appleAppId\",\"benefitDelivery\",\"benefitPayment\",\"benefitPrice\",\"benefitDeliveryTitle\",\"benefitPaymentTitle\",\"benefitPriceTitle\",\"commercialInfo\",\"confidential\",\"contacts\",\"copyright\",\"delivery\",\"email\",\"firebaseAndroidLink\",\"howToBuy\",\"mobileAppLinkIOS\",\"mobileLinkAndroid\",\"mobileAppLinkAppGallery\",\"paymentOrders\",\"phone\",\"phoneDelivery\",\"regulations\",\"returnPolicy\",\"schedule\",\"socialLinkInstagram\",\"socialLinkVK\",\"magDeliveryUrl\",\"magDeliveryToken\",\"yandexGeoApiKey\",\"yandexGeoApiKeyDev\",\"gtmId\",\"gtmIdDev\",\"yandexMetrikaId\",\"yandexMetrikaIdDev\",\"supplyContract\",\"consentToPersonalDataProcessing\",\"salesAndPurchaseAgreement\",\"promotionRules\",\"googleOptimizeExperimentId\",\"googleOptimizeExperimentIdDev\",\"productCatalogIdFB\",\"productCatalogIdVK\",\"linkToReviews\",\"geocoderToken\",\"geocoderTokenDev\",\"kdvExpressUrl\",\"orderInvoiceName\",\"orderInvoiceBankName\",\"orderInvoiceBankAcc\",\"orderInvoiceBankNumber\",\"hCaptchaKey\",\"recipes\"],\"deliveryAddressesFilter\":{\"isDraft\":false}}"}
          


def data_for_get_products(category_id:Union[int, str], limit:Union[int, str]):
    return {
        "query":"\n  query ($input: ProductsRequest, $productFilterTimeRangeUnit: PeriodEnum) {\n    products (input: $input) {\n      list {\n  id\n  code\n  name\n  description\n  \
amount\n  image {\n  id\n  title\n  alt\n}\n  price\n  previousPrice\n  itemSum\n  isNew\n  isHit\n  isVkusvill\n  isFavorite\n  isAvailable\n  isSubscribed\n  isVeterinaryControl\n  \
quant {\n  code\n  fullName\n  shortName\n  multiple\n  pricePerUnit\n  previousPricePerUnit\n  unit\n  type\n  minAmount\n  stepAmount\n  currency\n}\n  categories {\n  id\n  name\n  \
code\n  treeId\n  parentTreeId\n}\n  rating\n  numberOfRatings\n}\n      page {\n  total\n  limit\n  page\n}\n      filters {\n  type\n  name\n  title\n  ... on FilterList {\n    \
options {\n  id\n  value\n  label\n  count\n  isApplied\n}\n  }\n  ... on FilterTimeRange {\n    minValue (unit: $productFilterTimeRangeUnit)\n    maxValue \
(unit: $productFilterTimeRangeUnit)\n  }\n}\n      sort {\n  param\n  title\n  direct\n  isApplied\n}\n    }\n  }\n","variables":"{\"productFilterTimeRangeUnit\":\"month\",\"input\":\
{\"page\":{\"page\":1,\"limit\":" + str(limit) + "},\"sort\":{\"param\":\"default\",\"direct\":\"asc\"},\"filter\":{\"byCategoryId\":" + str(category_id) + "}}}"}













