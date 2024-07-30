db = db.getSiblingDB("create_alert");

db.price_alerts.drop();

db.price_alerts.insertMany([
    {
        "email": "test1@example.com",
        "product_name": "Product 1",
        "target_price": 100
    },
    {
        "email": "test2@example.com",
        "product_name": "Product 2",
        "target_price": 200
    }
]);
