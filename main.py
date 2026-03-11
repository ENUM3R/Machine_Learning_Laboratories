from ucimlrepo import fetch_ucirepo

def fetch_iris() -> None:
    # fetch IRIS dataset
    iris = fetch_ucirepo(id=53)

    # data (as pandas dataframes)
    X = iris.data.features
    y = iris.data.targets

    # metadata
    print(iris.metadata)

    # variable information
    print(iris.variables)

def fetch_glass() -> None:
    # fetch dataset
    glass_identification = fetch_ucirepo(id=42)

    # data (as pandas dataframes)
    X = glass_identification.data.features
    y = glass_identification.data.targets

    # metadata
    print(glass_identification.metadata)

    # variable information
    print(glass_identification.variables)

fetch_iris()
fetch_glass()