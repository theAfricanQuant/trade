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
# AST1
# {'price': 20.0, 'results': {}, 'quantity': 100}


# create some other occurrence with that subject.
# In this example, a sale of 20 units of the asset,
# for the price of $30.
other_occurrence = Occurrence(
		subject=some_asset,
		date='2018-01-03',
		quantity=-20,
		price=30
	)
holder.accumulate(other_occurrence)

# check the holder state. It should show a change in quantity
# and some profit:
for subject, subject_details in holder.subjects.items():
	print(subject)
	print(subject_details.state)
# AST1
# {'price': 20.0, 'results': {'trades': 200.0}, 'quantity': 80}


# create some other occurrence with that subject.
# Now a purchase of 10 units of the asset, for the
# price of $20.
another_occurrence = Occurrence(
		subject=some_asset,
		date='2018-01-04',
		quantity=10,
		price=25
	)
holder.accumulate(another_occurrence)

# check the holder state. It should show a change in quantity
# and in the value of the subject:
for subject, subject_details in holder.subjects.items():
	print(subject)
	print(subject_details.state)
# AST1
# {'price': 20.555555555555557, 'results': {'trades': 200.0}, 'quantity': 90}



# Contexts:
from trade.context import Context
from trade.context import fetch_daytrades

# An occurrence with a subject; a purchase of 10 units
# of the asset, for the price of $25.
occurrence_1 = Occurrence(
		subject=some_asset,
		date='2018-01-03',
		quantity=10,
		price=25
	)
# An occurrence with the same subject on the same day;
# a sale of 5 units of the asset, for the price of $30.
occurrence_2 = Occurrence(
		subject=some_asset,
		date='2018-01-03',
		quantity=-5,
		price=28
	)
# Creating a context with a list of occurrences and a list of
# rules; in this case, the fetch_daytrades() rule
some_context = Context(
		[occurrence_1, occurrence_2],
		[fetch_daytrades]
	)
# fetch_positions() apply all contexts rules.
some_context.fetch_occurrences()

# accumulate all occurrences in the context:
for occurrences in some_context.data['occurrences'].values():
    for the_occurrence in occurrences.values():
        holder.accumulate(the_occurrence)

# check the holder state. It should show some results related
# to daytrades:
for subject, subject_details in holder.subjects.items():
	print(subject)
	print(subject_details.state)
