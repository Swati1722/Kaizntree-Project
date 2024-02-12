import random
from faker import Faker  # Install faker using: pip install faker
from items.models import Items, Tag, Category  # Replace 'your_app' with the name of your Django app

fake = Faker()

# Create 20 items
for _ in range(20):
    # Create item
    item = Items(
        sku=fake.uuid4(),  # You can replace this with your own SKU generation logic
        name=fake.word(),
        in_stocks=random.randint(0, 100),
        available_stocks=random.randint(0, 100),
    )
    item.save()

    # Add random tags (1 to 3 tags per item)
    tags_count = random.randint(1, 3)
    tags = Tag.objects.order_by('?')[:tags_count]
    item.tags.set(tags)

    # Add random categories (1 to 2 categories per item)
    categories_count = random.randint(1, 2)
    categories = Category.objects.order_by('?')[:categories_count]
    item.category.set(categories)

print("20 items created successfully!")
