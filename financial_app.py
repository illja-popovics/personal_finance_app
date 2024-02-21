import argparse
from expense_classes import *


class FinancialApp:
    def __init__(self):
        self.parser = self.create_arg_parser()
        self.is_running = False
        self.account = None

    def create_arg_parser(self):
        """Create the argument parser."""
        parser = argparse.ArgumentParser(description="Financial Application")
        parser.add_argument(
            "action",
            choices=["expense", "income", "load", "exit"],
            help="Action to perform",
        )
        return parser

    def run(self):
        """Start the financial application."""
        self.is_running = True
        print("Welcome to the Financial Application!")

        while self.is_running:
            args = self.parser.parse_args(input("Enter your command: ").split())

            if args.action == "exit":
                self.is_running = False
                print("Exiting the Financial Application.")
            else:
                self.handle_action(args)

    def handle_action(self, args):
        """Handle the user's action."""
        if args.action == "expense":
            self.add_expense()
        elif args.action == "income":
            self.add_income()
        elif args.action == "load":
            self.load_registry()

    def add_expense(self):
        """Add an expense to the account."""
        if self.account == None:
            month = datetime.now().month
            self.account = AccountPerMonth(month)

        print("Adding expense...")

    def add_income(self):
        """Add an income to the account."""
        # Implement this method according to your application's logic
        print("Adding income...")

    def load_registry(self):
        """Load the registry from a file."""
        # Implement this method according to your application's logic
        print("Loading registry...")


# Example usage
if __name__ == "__main__":
    app = FinancialApp()
    app.run()
