from datetime import datetime, date

def get_birthday():
    """Get user's birthday from input."""
    while True:
        try:
            birthday_str = input("Enter your birthday (MM/DD/YYYY): ")
            birthday = datetime.strptime(birthday_str, "%m/%d/%Y").date()
            
            # Check if birthday is not in the future
            if birthday > date.today():
                print("Birthday cannot be in the future. Please try again.")
                continue
            
            return birthday
        except ValueError:
            print("Invalid date format. Please use MM/DD/YYYY format.")

def calculate_age_in_days(birthday):
    """Calculate age in days."""
    today = date.today()
    age_in_days = (today - birthday).days
    return age_in_days

def main():
    print("=== Birthday to Age Calculator ===")
    birthday = get_birthday()
    age_days = calculate_age_in_days(birthday)
    
    # Calculate years and remaining days for reference
    age_years = age_days // 365
    remaining_days = age_days % 365
    
    print(f"\nYour birthday: {birthday.strftime('%B %d, %Y')}")
    print(f"Your age: {age_days} days")
    print(f"(That's approximately {age_years} years and {remaining_days} days)")

if __name__ == "__main__":
    main()
