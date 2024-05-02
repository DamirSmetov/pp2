import psycopg2

conn = psycopg2.connect(host = "localhost", dbname = "postgres", user="postgres", password = "damir2005d", port = "5432")
conn.autocommit = True

#Function for finding name
with conn.cursor() as cur:
    cur.execute(
        """
        create or replace function fname(name varchar)
        returns table
        (
            id integer,
            username varchar(255),
            number varchar 
        )
        as
        $$
        begin
            RETURN QUERY
            select m.id,
                   m.username,
                  m.number
            from Phonebook m
            where m.username = name;
        end;
        $$
        Language plpgsql;
           
        """ 
    )
#Procedure for inserting data    
with conn.cursor() as cur:
    cur.execute(
        """
        create or replace procedure  Insert_data(name varchar, number varchar)
        language 'plpgsql'
        as
        $$
        begin
            if exists (select * from Phonebook where username = $1)then
                update Phonebook set number = $2 where username = $1;
            else
                insert into Phonebook (username, number) values ($1, $2);
            
            end if;
            
        commit; 
        end;
        $$
        
            
        """ 
    )
#function Limit and offset
with conn.cursor() as cur:
    cur.execute(
        """
        create or replace function flimit()
        returns table
        (
            id integer,
            username varchar(255),
            number varchar 
        )
        as
        $$
        begin
            RETURN QUERY
            select m.id,
                   m.username,
                  m.number
            from Phonebook m
            limit 4
            offset 3;
        end;
        $$
       Language plpgsql;
           
        """ 
    )
#Procedure for deleting data
with conn.cursor() as cur:
    cur.execute(
        """
        create or replace procedure  Delete_data(variable varchar)
        language 'plpgsql'
        as
        $$
        begin
            if exists (select * from Phonebook where $1 like '+%')then
                delete from Phonebook where number = $1;
            else
                delete from Phonebook where username = $1;
            end if; 
        commit; 
        end;
        $$
        
            
        """ 
    )
#Procedure for inserting many people
with conn.cursor() as cur:
    cur.execute(
        """
        create or replace procedure  Insert_many_users(p_names varchar [], p_phones varchar[], inout out_phones varchar[])
        language 'plpgsql'
        as
        $$
        declare
            i int;
        
        begin
            for i in 1..cardinality(p_names) LOOP
                if length(p_phones[i]) = 12  then
                    if exists (select * from Phonebook where username = p_names[i])then
                        update Phonebook set number = p_phones[i] where username = p_names[i];
                    else
                        insert into Phonebook(username, number) values (p_names[i], p_phones[i]);
                    end if;
                else
                    SELECT ARRAY_APPEND(out_phones, p_phones[i]) INTO out_phones;
                
                end if; 
            end LOOP;
        commit; 
        end;
        $$
        """ 
    )
    
        
        
        
        
        
        
