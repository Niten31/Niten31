CREATE TABLE snacks (
    id INT AUTO_INCREMENT PRIMARY KEY,
    product_name VARCHAR(255),
    brands VARCHAR(255),
    countries TEXT,
    quantity_value FLOAT,
    quantity_unit VARCHAR(10),
    nutriscore_grade VARCHAR(1),
    energy_kcal FLOAT
);
