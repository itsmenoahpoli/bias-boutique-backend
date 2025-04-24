from src.modules.products.products_service import products_service
import random

def generate_sku(category_code, index):
    return f"{category_code}{str(index).zfill(5)}"

def generate_price():
    # Generate random price between 200 and 10000
    base_price = round(random.uniform(200, 10000), 2)
    # 40% chance of having a discount
    is_discounted = random.random() < 0.4
    if is_discounted:
        discount_percentage = random.uniform(0.1, 0.3)  # 10-30% discount
        discounted_price = round(base_price * (1 - discount_percentage), 2)
    else:
        discounted_price = base_price
    return base_price, discounted_price, is_discounted

def generate_products_for_category(category, category_code, start_index):
    products = []
    
    # Category-specific attributes
    category_details = {
        "Albums": {
            "names": ["Limited Edition Album", "Special Package", "Deluxe Version", "Standard Edition", "Collector's Edition"],
            "groups": ["BlackPink", "BTS", "Twice", "Red Velvet", "EXO", "NCT", "ITZY", "Stray Kids", "IVE", "NewJeans"],
            "versions": ["Version A", "Version B", "Version C", "Member Version", "Group Version"],
        },
        "Photocards": {
            "types": ["Official PC", "Limited PC", "Season Greetings PC", "Concert PC", "Fanmeeting PC"],
            "members": ["Jisoo", "Jennie", "Rosé", "Lisa", "Jimin", "V", "Jungkook", "Suga", "RM", "Jin", "J-Hope"],
        },
        "Lightsticks": {
            "versions": ["Official Ver.1", "Official Ver.2", "Special Edition", "Anniversary Edition", "Concert Version"],
        },
        "Clothing": {
            "types": ["T-Shirt", "Hoodie", "Sweatshirt", "Cap", "Jacket", "Sweater"],
            "sizes": ["S", "M", "L", "XL"],
        },
        "Accessories": {
            "types": ["Ring", "Necklace", "Bracelet", "Earrings", "Phone Case", "Bag", "Keychain"],
        },
        "Stationary": {
            "types": ["Notebook", "Pen Set", "Sticker Set", "Planner", "Diary", "Pencil Case"],
        },
        "Beauty Products": {
            "types": ["Lip Tint", "Face Mask", "Cushion", "Hand Cream", "Perfume", "Eye Shadow"],
        },
        "Home Goods": {
            "types": ["Pillow", "Blanket", "Mug", "Poster", "Frame", "Plushie", "Room Decor"],
        }
    }

    for i in range(50):
        index = start_index + i
        sku = generate_sku(category_code, index)
        
        # Generate name based on category
        if category == "Albums":
            name = f"{random.choice(category_details[category]['groups'])} - {random.choice(category_details[category]['names'])} {random.choice(category_details[category]['versions'])}"
        elif category == "Photocards":
            name = f"{random.choice(category_details[category]['members'])} {random.choice(category_details[category]['types'])}"
        elif category == "Lightsticks":
            name = f"{random.choice(category_details[category]['versions'])} Lightstick"
        else:
            name = f"{random.choice(category_details[category]['types'])} - {category} Collection"

        price, discounted_price, is_discounted = generate_price()
        stocks_qty = random.randint(10, 200)

        product = {
            "sku": sku,
            "name": name,
            "category": category,
            "description": f"Official K-pop merchandise: {name}. High-quality {category.lower()} for true fans.",
            "price": price,
            "discounted_price": discounted_price,
            "stocks_qty": stocks_qty,
            "is_discounted": is_discounted,
            "is_pulished": True,
            "image": "https://placehold.co/600x400"
        }
        products.append(product)
    
    return products

def seed_products():
    categories = {
        "Albums": "ALB",
        "Photocards": "PCD",
        "Lightsticks": "LTS",
        "Clothing": "CLT",
        "Accessories": "ACC",
        "Stationary": "STN",
        "Beauty Products": "BTY",
        "Home Goods": "HMG"
    }
    
    start_index = 1
    for category, category_code in categories.items():
        print(f"\nSeeding {category}...")
        products = generate_products_for_category(category, category_code, start_index)
        
        for product in products:
            try:
                products_service.create_data(product, 'sku')
                print(f"Created product: {product['name']}")
            except Exception as e:
                print(f"Error creating product {product['name']}: {str(e)}")
        
        start_index += 50
    
    print("\nProduct seeding completed!")
