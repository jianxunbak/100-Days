import requests


class Brew:
    def __init__(self, name=None, country=None):
        self.all_breweries = 'https://api.openbrewerydb.org/v1/breweries/'
        self.breweries = []
        self.page = 1
        self.per_page = 50
        self.brew_name = name
        self.brew_country = country

    def get_breweries(self):
        print('getting all breweries')
        params = {'per_page': self.per_page,
                  'page': self.page, }
        if self.brew_name:
            params['by_name'] = self.brew_name
        if self.brew_country:
            params['by_country'] = self.brew_country
        print(params)

        while True:
            print(f'Fetching page {params["page"]} with params: {params}')
            response = requests.get(url=self.all_breweries, params=params)
            print(f'Status Code: {response.status_code}')
            if response.status_code == 200:
                data = response.json()
                if not data:
                    print('No more data found. Exiting loop.')
                    break
                self.breweries.extend(data)
                params['page'] += 1
            else:
                print(f'Error: Received status code {response.status_code}')
                break
        print('got all breweries')
        return self.breweries

    def convert_data(self):
        print('converting data')
        selected_detail_list = []
        for brewery in self.breweries:
            address = [brewery.get('address_1'),
                       brewery.get('address_2'),
                       brewery.get('address_3'), ]
            join_address = ','.join(filter(None, address))
            country = brewery.get('country')
            name = brewery.get('name')
            website = brewery.get('website_url')
            phone = brewery.get('phone')
            selected_details = {'name': name,
                                'address': join_address,
                                'website': website,
                                'phone': phone,
                                'country': country}
            selected_detail_list.append(selected_details)
        print('converted data')
        return selected_detail_list

    def brew_metadata(self):
        response = requests.get(url=self.all_breweries + '/meta')
        if response.status_code == 200:
            data = response.json()
            return data['total']
        else:
            response.raise_for_status()
