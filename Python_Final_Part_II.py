import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("airbnb_listings.csv")

# 1.
def neighborhoods(data):
    dublin_data = data[data['neighbourhood'] == 'Dublin']
    avg_scores = dublin_data.groupby('neighbourhood_cleansed')['review_scores_rating'].mean().sort_values(ascending=False).head(5)
    plt.figure(figsize=(10, 6))
    avg_scores.plot(kind='pie')
    plt.title('Top 5 Neighborhoods in Dublin by Average Review Score')
    plt.ylabel('')
    plt.show()
    pass

# 2.
def numbers_of_bedrooms(data):
    data['price'] = data['price'].replace('[\$,]', '', regex=True).astype(float)
    three_bedrooms = data[(data['bedrooms'] == 3) & (data['neighbourhood'] == 'Dublin')]
    plt.figure(figsize=(10, 6))
    sns.boxplot(data=three_bedrooms, x='price')
    plt.title('Price Distribution of 3-Bedroom Properties in Dublin')
    plt.xlabel('Price')
    plt.show()

# 3.
def numbers_of_listings(data):
    print("Identify hosts who have more than 2 listings. Display their profiles in a tabular format")
    listings_count = data['host_id'].value_counts()
    multiple_listings = listings_count[listings_count > 2]
    profiles = pd.DataFrame({'host_id': multiple_listings.index, 'number_of_listings': multiple_listings.values})
    print(profiles.to_string(index=False))
    pass

# Main function to run the command-line interface
def main(data):
    while True:
        print("\nMain Menu")
        print("1. Find the top 5 neighborhoods with the highest average review scores in Dublin")
        print("2. List all available properties in Dublin with 3 bedrooms")
        print("3. Identify hosts who have more than 2 listings")
        print("0. Exit")
        choice = input("Enter your choice (write the number only): ")

        if choice == "1":
            neighborhoods(data)
        elif choice == "2":
            numbers_of_bedrooms(data)
        elif choice == "3":
            numbers_of_listings(data)
        elif choice == "0":
            print("Exiting program.")
            break
        else:
            print("Invalid choice, please try again.")

if data is not None:
    main(data)
else:
    print("Failed to load data, program will exit.")