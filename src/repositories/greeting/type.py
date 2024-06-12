from src.repositories.greeting import in_memory, postgres

GreetingRepo = in_memory.GreetingRepo | postgres.GreetingRepo
