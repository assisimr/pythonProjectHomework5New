CREATE DATABASE gradesData;
use gradesData;

CREATE TABLE IF NOT EXISTS tblGradesImport (
    `LastName` VARCHAR(12) CHARACTER SET utf8,
    `FirstName` VARCHAR(16) CHARACTER SET utf8,
    `Ssn` VARCHAR(21) CHARACTER SET utf8,
    `Test1` INT,
    `Test2` INT,
    `Test3` INT,
    `Final` INT,
    `Grade` VARCHAR(7) CHARACTER SET utf8
);
INSERT INTO tblGradesImport VALUES
    ('Alfalfa','   "Aloysius"','   "123-45-6789"',40,90,100,49,'   "D-"'),
    ('Alfred','    "University"',' "123-12-1234"',41,97,96,48,'   "D+"'),
    ('Gerty','     "Gramma"','     "567-89-0123"',41,80,60,44,'   "C"'),
    ('Android','   "Electric"','   "087-65-4321"',42,23,36,47,'   "B-"'),
    ('Bumpkin','   "Fred"','       "456-78-9012"',43,78,88,45,'   "A-"'),
    ('Rubble','    "Betty"','      "234-56-7890"',44,90,80,46,'   "C-"'),
    ('Noshow','    "Cecil"','      "345-67-8901"',45,11,-1,43,'   "F"'),
    ('Buff','      "Bif"','        "632-79-9939"',46,20,30,50,'   "B+"'),
    ('Backus','    "Jim"','        "143-12-1234"',48,1,97,97,'   "A+"'),
    ('Carnivore',' "Art"','        "565-89-0123"',44,1,80,40,'   "D+"'),
    ('Dandy','     "Jim"','        "087-75-4321"',47,1,23,45,'   "C+"'),
    ('Elephant','  "Ima"','        "456-71-9012"',45,1,78,77,'   "B-"'),
    ('Franklin','  "Benny"','      "234-56-2890"',50,1,90,90,'   "B-"'),
    ('George','    "Boy"','        "345-67-3901"',40,1,11,4,'   "B"'),
    ('Heffalump',' "Harvey"','     "632-79-9439"',30,1,20,40,'   "C"');