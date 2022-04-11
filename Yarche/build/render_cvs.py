




FirstTitle = (
    'id',
    'name'
)


TitleCategory = (
    'id', 
    'name',
    'code',
    'treeId',
    'parentTreeId',
    'description',
    'amount',
    'img_id', 
    'img_title', 
    'metaTags_title', 
    'metaTags_value',
    'isBold')



def getCategory(inside:dict):
    return(
        inside.get('id', None),
        inside.get('name', None),
        inside.get('code', None),
        inside.get('treeId', None),
        inside.get('parentTreeId', None),
        inside.get('description', None),
        inside.get('amount', None),
        inside['image'].get('id', None) if inside['image'] else None,
        inside['image'].get('title', None) if inside['image'] else None,
        inside['metaTags'][0].get('value', None),
        inside['metaTags'][1].get('value', None),
        inside.get('description', None),
        )
   


TitleProduct = (
    "id",
    "code",
    "name",
    "description",
    "amount",
    "img_id", 
    "img_title",
    "price",
    "previousPrice",
    "itemSum",
    "isNew",
    "isHit",
    "isVkusvill",
    "isFavorite",
    "isAvailable",
    "isSubscribed",
    "isVeterinaryControl",
    "currency",
    "rating",
    "numberOfRatings")



def getProduct(inside:dict):
    return(
        inside.get('id', None),
        inside.get('code', None),
        inside.get('name', None),
        inside.get('description', None),
        inside.get('amount', None),
        inside['image'].get('id', None) if inside['image'] else None,
        inside['image'].get('title', None) if inside['image'] else None,
        inside.get('price', None),
        inside.get('previousPrice', None),
        inside.get('itemSum', None),
        inside.get('isNew', None),
        inside.get('isHit', None),
        inside.get('isVkusvill', None),
        inside.get('isFavorite', None),
        inside.get('isAvailable', None),
        inside.get('isSubscribed', None),
        inside.get('isVeterinaryControl', None),
        inside['quant'].get('currency', "RUB"),
        inside.get('rating', None),
        inside.get('numberOfRatings', None)
        )
