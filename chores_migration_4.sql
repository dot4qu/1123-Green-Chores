-- this is not going work for a straight run, this is specific to the state the db was in when brax needed to be dropped
-- aka DONT RUN THIS

DELETE FROM People WHERE Name='Braxton';
DELETE FROM Chores WHERE ID=3;
UPDATE Chores SET Name='Mop stairs and clean/organize living room througout week' WHERE ID=2;
UPDATE Chores SET ID=ID-1 WHERE ID > 3;
UPDATE People SET ID=ID-1 WHERE ID > 8;
UPDATE People SET ChoreId=ChoreId - 1 WHERE ChoreId > 1;
