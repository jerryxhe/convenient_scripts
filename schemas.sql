CREATE TABLE wsj_gdrive (
issue DATE NOT NULL,
section varchar(4) NOT NULL,
pdf_hash VARCHAR(1023) NOT NULL,
gdrive_id VARCHAR(1023) NOT NULL,
ne varchar(127)[],
metadata jsonb
);

CREATE TABLE sentence_translations ( 
article_id varchar(11) NOT NULL,     
sentence varchar(2047) NOT NULL, 
num INT NOT NULL, 
words varchar(127)[], 
pos varchar(8)[],                                                                           
hash varchar(63) NOT NULL, 
google_translation varchar(4095),  
alternative_translations jsonb
)
