DELETE FROM People WHERE Name='Braxton';
DELETE FROM Chores WHERE ID=3;
UPDATE Chores SET Name='Mop stairs and clean/organize living room througout week' WHERE ID=2;
UPDATE Chores SET ID=ID-1 WHERE ID > 3;
UPDATE People SET ID=ID-1 WHERE ID > 8;