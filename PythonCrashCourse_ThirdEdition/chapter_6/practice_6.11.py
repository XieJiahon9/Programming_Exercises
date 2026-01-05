#练习6.11 城市：创建一个名为cities的字典，将三个城市名用作键。
#对于每座城市，都创建一个字典，并在其中包含该城市所属的国家、人口约数以及一个有关该城市的事实。
#表示每座城市的字典都应包含country、population和fact等键。将每座城市的名字以及相关信息都打印出来。
cities = {
    'Fuzhou': {
        'country': 'China',
        'population': 8_400_000,
        'fact': 'Nicknamed"Banyan City".'
    },
    'Reykjavik': {
        'country': 'Iceland',
        'population': 240_000,
        'fact': "The world's northernmost capital."},
    'New York': {
        'country': 'United States',
        'population': 8_800_000,
        'fact': 'The Statue of liberty was a gift from France.'},
}
for city, info in cities.items():
    print(f"City: {city.title()}")
    for attribute, content in info.items():
        print(f"{attribute.title()}: {content}")
    print("-----------------------------------------")