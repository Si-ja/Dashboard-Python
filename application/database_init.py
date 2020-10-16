def create_populate_db():
    """
    Call this method in order to to create a new database and populate it with information
    from your excel files.
    """
    from config_handlers.db_management.populate_db import DatabasePopulation
    db_pop = DatabasePopulation()
    db_pop.handler()

if __name__ == "__main__":
    create_populate_db()
