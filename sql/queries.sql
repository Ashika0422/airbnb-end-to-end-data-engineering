SELECT COUNT(*) AS Total_Listings
FROM listings;

SELECT AVG(price) AS Average_Price
FROM listings;

SELECT room_type,
       COUNT(*) AS Total
FROM listings
GROUP BY room_type
ORDER BY Total DESC;

SELECT name,
       neighbourhood_cleansed,
       price
FROM listings
ORDER BY price DESC
LIMIT 10;

SELECT AVG(review_scores_rating)
FROM listings;

SELECT host_is_superhost,
       COUNT(*)
FROM listings
GROUP BY host_is_superhost;

