from trade.holder import Holder
from trade.occurrence import Occurrence
from trade.subject import Subject

# create a holder
holder = Holder()

# define some subject
some_asset = Subject('AST1')

# create an occurrence with that subject.
# In this example, a purchase of 100 units of the asset,
# for the value of $20.
some_occurrence = Occurrence(
		some_asset,
		'2018-01-02',
		{
			"quantity": 100,
			"value": 20
		}
	)

# pass it to the holder
holder.trade(some_occurrence)

# check the holder state:
for subject, state in holder.state.items():
	print(subject)
	print(state)
# AST1
# {'value': 20.0, 'quantity': 100}


# create some other occurrence with that subject.
# In this example, a sale of 20 units of the asset,
# for the value of $30.
holder.trade(Occurrence(
		some_asset,
		'2018-01-03',
		{
			"quantity": -20,
			"value": 30
		}
	))

# check the holder state. It should show a change in quantity
# and some profit:
for subject, state in holder.state.items():
	print(subject)
	print(state)
# AST1
# {'value': 20.0, 'quantity': 80}


# create some other occurrence with that subject.
# Now a purchase of 10 units of the asset, for the
# value of $20.
holder.trade(Occurrence(
		some_asset,
		'2018-01-04',
		{
			"quantity": 10,
			"value": 25
		}
	))

# check the holder state. It should show a change in quantity
# and in the value of the subject:
for subject, state in holder.state.items():
	print(subject)
	print(state)
# AST1
# {'value': 20.555555555555557, 'quantity': 90}
