from .product_seeder import seed_products

def run_all_seeders():
    print("Starting database seeding...")
    seed_products()
    print("Database seeding completed!")

if __name__ == "__main__":
    run_all_seeders()