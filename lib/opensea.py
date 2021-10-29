import json
import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder


class API:
    url = "https://api.opensea.io/graphql/"
    session = requests.session()
    // fill in from cookies submitted throught he web requests during a browser session
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36',
        'Connection': 'keep-alive',
        'X-API-KEY': '',
        'X-BUILD-ID': '',
        'X-VIEWER-ADDRESS': '',
        'X-VIEWER-CHAIN': 'ETHEREUM',
        'Authorization': ''
    }

    def __init__(self):
        self.session.headers = self.headers

    def addItem(self, collection_name, description, url_link, wallet_address, name, image):
        ql_query = {
            "query": "mutation collectionManagerAssetCreateMutation(\n  $assetContract: AssetContractRelayID\n  $collection: CollectionSlug!\n  $description: String\n  $externalLink: URL\n  $identity: IdentityInputType!\n  $imageFile: Upload\n  $maxSupply: String\n  $mediaFile: Upload\n  $name: String!\n  $tokenId: String\n  $chain: ChainScalar\n  $unlockableContent: String\n  $isNsfw: Boolean!\n  $properties: [StringTraitConfig!]\n  $levels: [NumericTraitConfig!]\n  $stats: [NumericTraitConfig!]\n) {\n  assets {\n    create(assetContract: $assetContract, collection: $collection, description: $description, externalLink: $externalLink, imageFile: $imageFile, maxSupply: $maxSupply, mediaFile: $mediaFile, name: $name, tokenId: $tokenId, chain: $chain, unlockableContent: $unlockableContent, isNsfw: $isNsfw, properties: $properties, levels: $levels, stats: $stats, identity: $identity) {\n      tokenId\n      assetContract {\n        address\n        chain\n        id\n      }\n      ...asset_url\n      ...itemEvents_data\n      id\n    }\n  }\n}\n\nfragment asset_url on AssetType {\n  assetContract {\n    account {\n      address\n      chain {\n        identifier\n        id\n      }\n      id\n    }\n    id\n  }\n  tokenId\n}\n\nfragment itemEvents_data on AssetType {\n  assetContract {\n    address\n    chain\n    id\n  }\n  tokenId\n}\n",
            "variables": {
                "assetContract": None,
                "collection": collection_name,
                "description": description,
                "externalLink": url_link,
                "identity": {"address": wallet_address, "chain": "ETHEREUM"},
                "imageFile": None,
                "maxSupply": "1",
                "mediaFile": None,
                "name": name,
                "tokenId": None,
                "chain": "ETHEREUM",
                "unlockableContent": "",
                "isNsfw": False,
                "properties": [],
                "levels": [],
                "stats": []
            },
        }

        imageFile = {
            "filename": "",
            "path": "",
            "mimetype": ""
        }

        multi_data = MultipartEncoder(
            fields={
                'operations': json.dumps(ql_query),
                'map': json.dumps({'1': ["variables.imageFile"]}),
                '1': (imageFile["filename"], open('%s/%s' % (imageFile["path"], imageFile["filename"]), 'rb'), imageFile["mimetype"]),
            }
        )
        self.headers.update({'Content-Type': multi_data.content_type})
        print(self.session.post(self.url, headers=self.headers, data=multi_data).text)

    def remove(self):
        payload = {
            "id": "collectionManagerAssetEditDeleteMutation",
            "query": "mutation collectionManagerAssetEditDeleteMutation(\n  $asset: AssetRelayID!\n) {\n  assets {\n    delete(asset: $asset) {\n      relayId\n      id\n    }\n  }\n}\n",
            "variables": {
                "asset": "" # item to remove
            }
        }

        del self.headers['Content-Type']
        print(self.session.post(self.url, headers=self.headers, json=payload).text)

    def addCollection(self):
        ql_query = {
            "query": "mutation collectionManagerCreateOrEditCreateMutation(\n  $input: CollectionCreateMutationDataTypeInput!\n) {\n  collections {\n    create(collectionInput: $input) {\n      slug\n      id\n    }\n  }\n}\n",
            "variables": {
                "input": {
                    "bannerImage": None,
                    "defaultChain": "ETHEREUM",
                    "description": "",
                    "devSellerFeeBasisPoints": 1,
                    "displayData": {"cardDisplayStyle": "CONTAIN"},
                    "externalUrl": "", # link back web address
                    "featuredImage": None,
                    "instagramUsername": "",
                    "logoImage": None,
                    "mediumUsername": "",
                    "name": "",
                    "slug": "",
                    "paymentAssets": ["", "", "", ""],
                    "payoutAddress": "",
                    "twitterUsername": "",
                    "isNsfw": False
                }
            }
        }

        bannerImage = {
            "filename": "",
            "path": "",
            "mimetype": ""
        }

        featuredImage = {
            "filename": "",
            "path": "",
            "mimetype": ""
        }

        logoImage = {
            "filename": "",
            "path": "",
            "mimetype": ""
        }

        multi_data = MultipartEncoder(
            fields={
                'operations': json.dumps(ql_query),
                'map': json.dumps({"1": ["variables.input.bannerImage"], "2": ["variables.input.featuredImage"], "3": ["variables.input.logoImage"]}),
                '1': (bannerImage["filename"], open('%s/%s' % (bannerImage["path"], bannerImage["filename"]), 'rb'), bannerImage["mimetype"]),
                '2': (featuredImage["filename"], open('%s/%s' % (featuredImage["path"], featuredImage["filename"]), 'rb'), featuredImage["mimetype"]),
                '3': (logoImage["filename"], open('%s/%s' % (logoImage["path"], logoImage["filename"]), 'rb'), logoImage["mimetype"]),
            }
        )
        self.headers.update({'Content-Type': multi_data.content_type})
        print(self.session.post(self.url, headers=self.headers, data=multi_data).text)

    def debug(self):
        ql_query = {
            "query": "mutation collectionManagerAssetCreateMutation(\n  $assetContract: AssetContractRelayID\n  $collection: CollectionSlug!\n  $description: String\n  $externalLink: URL\n  $identity: IdentityInputType!\n  $imageFile: Upload\n  $maxSupply: String\n  $mediaFile: Upload\n  $name: String!\n  $tokenId: String\n  $chain: ChainScalar\n  $unlockableContent: String\n  $isNsfw: Boolean!\n  $properties: [StringTraitConfig!]\n  $levels: [NumericTraitConfig!]\n  $stats: [NumericTraitConfig!]\n) {\n  assets {\n    create(assetContract: $assetContract, collection: $collection, description: $description, externalLink: $externalLink, imageFile: $imageFile, maxSupply: $maxSupply, mediaFile: $mediaFile, name: $name, tokenId: $tokenId, chain: $chain, unlockableContent: $unlockableContent, isNsfw: $isNsfw, properties: $properties, levels: $levels, stats: $stats, identity: $identity) {\n      tokenId\n      assetContract {\n        address\n        chain\n        id\n      }\n      ...asset_url\n      ...itemEvents_data\n      id\n    }\n  }\n}\n\nfragment asset_url on AssetType {\n  assetContract {\n    account {\n      address\n      chain {\n        identifier\n        id\n      }\n      id\n    }\n    id\n  }\n  tokenId\n}\n\nfragment itemEvents_data on AssetType {\n  assetContract {\n    address\n    chain\n    id\n  }\n  tokenId\n}\n",
            "variables": {
                "assetContract": None,
                "collection": "",
                "description": "",
                "externalLink": "",
                "identity": {"address": "", "chain": "ETHEREUM"},
                "imageFile": None,
                "maxSupply": "1",
                "mediaFile": None,
                "name": "",
                "tokenId": None,
                "chain": "ETHEREUM",
                "unlockableContent": "",
                "isNsfw": False,
                "properties": [],
                "levels": [],
                "stats": []
            },
        }

        imageFile = {
            "filename": "",
            "path": "files",
            "mimetype": "image/jpeg"
        }

        multi_data = MultipartEncoder(
            fields={
                'operations': json.dumps(ql_query),
                'map': json.dumps({'1': ["variables.imageFile"]}),
                '1': (imageFile["filename"], open('%s/%s' % (imageFile["path"], imageFile["filename"]), 'rb'), imageFile["mimetype"])
            }
        )

        self.headers.update({'Content-Type': multi_data.content_type})
        print(self.session.post(self.url, headers=self.headers, data=multi_data).text)


if __name__ == "__main__":
    main = API()
    main.debug()
