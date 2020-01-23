sql_create_table = """ CREATE TABLE IF NOT EXISTS bdos (
                                                       id integer PRIMARY KEY AUTOINCREMENT,
                                                       name text NOT NULL,
                                                       password text NOT NULL
                                                   ); 
CREATE TABLE IF NOT EXISTS gpms (
                                                   id integer PRIMARY KEY AUTOINCREMENT,
                                                   name text NOT NULL,
                                                   password text NOT NULL,
                                                   district text NOT NULL,
                                                   state text NOT NULL,
                                                   pincode text NOT NULL,
                                                   bdo_id integer,
                                                   FOREIGN KEY (bdo_id) REFERENCES bdos (id)
                                               );
CREATE TABLE IF NOT EXISTS projects (
                                                   id integer PRIMARY KEY AUTOINCREMENT,
                                                   name text NOT NULL,
                                                   category text NOT NULL,
                                                   area text NOT NULL,
                                                   state text NOT NULL,
                                                   labours integer NOT NULL,
                                                   cost integer NOT NULL,
                                                   start_date text NOT NULL,
                                                   end_date text,
                                                   bdo_id integer,
                                                   FOREIGN KEY (bdo_id) REFERENCES bdos (id)
                                               );

CREATE TABLE IF NOT EXISTS members (
                                                   id integer PRIMARY KEY AUTOINCREMENT,
                                                   name text NOT NULL,
                                                   password text NOT NULL,
                                                   district text NOT NULL,
                                                   state text NOT NULL,
                                                   age integer NOT NULL,
                                                   gender text NOT NULL,
                                                   address text NOT NULL,
                                                   working_days integer NOT NULL,
                                                   attendance integer NOT NULL,
                                                   is_card_issued text DEFAULT 'False',
                                                   gpm_id integer,
                                                   FOREIGN KEY (gpm_id) REFERENCES gpms (id)
                                               );

CREATE TABLE IF NOT EXISTS tasks (
                                                   id integer PRIMARY KEY AUTOINCREMENT,
                                                   wage integer NOT NULL,
                                                   wage_status text DEFAULT 'Requested',
                                                   complain text,
                                                   complain_status text DEFAULT 'Requested',
                                                   project_status text DEFAULT 'Requested',
                                                   member_id integer,
                                                   project_id integer,
                                                   FOREIGN KEY (member_id) REFERENCES members (id),
                                                   FOREIGN KEY (project_id) REFERENCES projects (id)
                                               );"""