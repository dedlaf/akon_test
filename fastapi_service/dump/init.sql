-- Вставка данных в таблицу customers
INSERT INTO customers (id, name) VALUES (1, 'John Doe');
INSERT INTO customers (id, name) VALUES (2, 'Jane Smith');
INSERT INTO customers (id, name) VALUES (3, 'Alice Johnson');
INSERT INTO customers (id, name) VALUES (4, 'Bob Brown');

-- Вставка данных в таблицу traffic
INSERT INTO traffic (customer_id, ip, date, received_traffic) VALUES (1, '192.168.218.159', '2022-01-05 10:15:00', 150.00);
INSERT INTO traffic (customer_id, ip, date, received_traffic) VALUES (2, '192.168.5.110', '2022-07-15 13:45:00', 200.00);
INSERT INTO traffic (customer_id, ip, date, received_traffic) VALUES (3, '192.168.3.45', '2023-02-12 09:30:00', 175.00);
INSERT INTO traffic (customer_id, ip, date, received_traffic) VALUES (4, '192.168.10.5', '2023-05-23 14:50:00', 220.00);
INSERT INTO traffic (customer_id, ip, date, received_traffic) VALUES (1, '192.168.218.159', '2023-03-01 16:30:00', 100.00);
INSERT INTO traffic (customer_id, ip, date, received_traffic) VALUES (2, '192.168.5.110', '2023-07-10 11:20:00', 130.00);
INSERT INTO traffic (customer_id, ip, date, received_traffic) VALUES (3, '192.168.3.45', '2023-11-20 17:00:00', 185.00);
INSERT INTO traffic (customer_id, ip, date, received_traffic) VALUES (4, '192.168.10.5', '2024-01-15 12:00:00', 210.00);
INSERT INTO traffic (customer_id, ip, date, received_traffic) VALUES (1, '192.168.218.159', '2024-02-05 10:15:00', 160.00);
INSERT INTO traffic (customer_id, ip, date, received_traffic) VALUES (2, '192.168.5.110', '2024-06-12 09:45:00', 230.00);
INSERT INTO traffic (customer_id, ip, date, received_traffic) VALUES (3, '192.168.3.45', '2024-08-08 10:00:00', 170.00);
INSERT INTO traffic (customer_id, ip, date, received_traffic) VALUES (4, '192.168.10.5', '2024-11-19 18:30:00', 240.00);
