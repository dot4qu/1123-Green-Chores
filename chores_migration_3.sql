-- Drop and recreate easiest way to rename and reorder IDs due to FK
DROP TABLE Chores;
CREATE TABLE Chores (
	ID INTEGER PRIMARY KEY,
	Name varchar(255) NOT NULL
);

INSERT INTO Chores (Name)
VALUES ('Trash cans'),
('Mop stairs'),
('Clean and organize living room'),
('Dish washer'),
('Clean kitchen counters and island'),
('Sweep & swiffer hallway floors'),
('Mop kitchen floor'),
('Clean bathroom and kitchen sink'),
('Organize laundry room'),
('Drying rack'),
('Wipe stovetop, clean and organize deck');

-- Matching up everyone with correct chore for week starting 7/23/18
UPDATE People
SET ChoreId = (
	SELECT ID
	FROM Chores 
	WHERE
		Name = 'Trash cans'
	)
WHERE
	Name = 'Braxton';

UPDATE People
SET ChoreId = (
	SELECT ID
	FROM Chores 
	WHERE
		Name = 'Mop stairs'
	)
WHERE
	Name = 'Shang';

UPDATE People
SET ChoreId = (
	SELECT ID
	FROM Chores 
	WHERE
		Name = 'Clean and organize living room'
	)
WHERE
	Name = 'DJ';

UPDATE People
SET ChoreId = (
	SELECT ID
	FROM Chores 
	WHERE
		Name = 'Dish washer'
	)
WHERE
	Name = 'AK';

UPDATE People
SET ChoreId = (
	SELECT ID
	FROM Chores 
	WHERE
		Name = 'Clean kitchen counters and island'
	)
WHERE
	Name = 'Byron';

UPDATE People
SET ChoreId = (
	SELECT ID
	FROM Chores 
	WHERE
		Name = 'Sweep & swiffer hallway floors'
	)
WHERE
	Name = 'Raghav';

UPDATE People
SET ChoreId = (
	SELECT ID
	FROM Chores 
	WHERE
		Name = 'Mop kitchen floor'
	)
WHERE
	Name = 'Josh';

UPDATE People
SET ChoreId = (
	SELECT ID
	FROM Chores 
	WHERE
		Name = 'Clean bathroom and kitchen sink'
	)
WHERE
	Name = 'Sweeney';

UPDATE People
SET ChoreId = (
	SELECT ID
	FROM Chores 
	WHERE
		Name = 'Organize laundry room'
	)
WHERE
	Name = 'BTeam';

UPDATE People
SET ChoreId = (
	SELECT ID
	FROM Chores 
	WHERE
		Name = 'Drying rack'
	)
WHERE
	Name = 'Ross';

UPDATE People
SET ChoreId = (
	SELECT ID
	FROM Chores 
	WHERE
		Name = 'Wipe stovetop, clean and organize deck'
	)
WHERE
	Name = 'BOD';