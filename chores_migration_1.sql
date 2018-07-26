CREATE TABLE Chores (
	ID INTEGER PRIMARY KEY,
	Name varchar(255) NOT NULL
);

CREATE TABLE People (
	ID INTEGER PRIMARY KEY,
	Name varchar(255) NOT NULL,
	Email varchar(255),
	ChoreID varchar(255),
	FOREIGN KEY (ChoreID) REFERENCES Chores(ID)
);

INSERT INTO People (Name)
VALUES ('Ryan'),
('Raghav'),
('Byron'),
('AK'),
('Sweeney'),
('BTeam'),
('Ross'),
('BOD'),
('Braxton'),
('DJ'),
('Shang');

INSERT INTO Chores (Name)
VALUES ('Trash cans'),
('Dish washer'),
('Drying rack'),
('Mop kitchen floor'),
('Clean and organize living room'),
('Clean kitchen counters and island'),
('Sweep hallway floors, organize laundry room'),
('Clean bathroom'),
('Wipe stovetop, clean and organize deck'),
('Mop stairs');