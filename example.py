from trade.holder import Holder
from trade.occurrence import Occurrence
from trade.subject import Subject

# create a holder
holder = Holder()

# define some subject
some_asset = Subject('AST1', 'Some Asset')

# create an occurrence with that subject.
# In this example, a purchase of 100 units of the asset,
# for the price of $20.
some_occurrence = Occurrence(
		subject=some_asset,
		date='2018-01-02',
		quantity=100,
		price=20
	)

# pass it to the holder
holder.accumulate(some_occurrence)

# check the holder state:
for subject, subject_details in holder.subjects.items():
	print(subject)
	print(subject_details.state)

# create some other occurrence with that subject.
# In this example, a sale of 20 units of the asset,
# for the price of $30.
other_occurrence = Occurrence(
		subject=some_asset,
		date='2018-01-02',
		quantity=-20,
		price=30
	)
holder.accumulate(other_occurrence)

# check the holder state. It should show a change in quantity
# and some profit:
for subject, subject_details in holder.subjects.items():
	print(subject)
	print(subject_details.state)


# create some other occurrence with that subject.
# Now a purchase of 10 units of the asset, for the
# price of $20.
another_occurrence = Occurrence(
		subject=some_asset,
		date='2018-01-02',
		quantity=10,
		price=25
	)
holder.accumulate(another_occurrence)

# check the holder state. It should show a change in quantity
# and in the value of the subject:
for subject, subject_details in holder.subjects.items():
	print(subject)
	print(subject_details.state)
