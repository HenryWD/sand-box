from bs4 import BeautifulSoup


def get_description(container):
    # Find all the product items on the page
    desc = container.find_all("div", class_="product-page-header__description collapsed ng-star-inserted")
    for p in desc:
        return (p.text.strip())


def get_details(container):
    descriptions = container.find_all("div", class_ = "ng-star-inserted storefront-page-phase-4")
    l = []
    d = dict()
    for i in descriptions:
        l.append(i.text.strip())

    for i in l:
        colon_pos = i.find(":")
        d[i[:colon_pos]] = i[colon_pos+1:]

    return d

def get_seller(soup):
    d = {}
    seller = soup.find("div",class_="storefront-header__content-subtitle__box")
    d["Seller"] = seller.text.strip()