
use conv_db;

CREATE TABLE df_ministop_oneplusone as SELECT *from flask_db.df_oneplusone ;
CREATE TABLE df_ministop_twoplusone as SELECT *from flask_db.df_twoplusone ;
CREATE TABLE df_ministop_dum as SELECT *from flask_db.df_dum ;
CREATE TABLE df_ministop_discount as SELECT *from flask_db.df_discount ;



CREATE TABLE df_cu_oneplusone as SELECT *from cu.df_cu_oneplusone ;
CREATE TABLE df_cu_twoplusone as SELECT *from cu.df_cu_twoplusone ;
CREATE TABLE df_cu_dum as SELECT *from cu.df_cu_dum ;
CREATE TABLE df_cu_threeplusone as SELECT *from cu.df_cu_threeplusone ;


CREATE TABLE df_emart24_oneplusone as SELECT *from emart24.df_emart24_oneplusone ;
CREATE TABLE df_emart24_twoplusone as SELECT *from emart24.df_emart24_twoplusone ;
CREATE TABLE df_emart24_dum as SELECT *from  emart24.df_emart24_threeplusone;
CREATE TABLE df_emart24_threeplusone as SELECT *from emart24.df_emart24_dum ;
CREATE TABLE df_emart24_discount as SELECT *from emart24.df_emart24_discount ;


CREATE TABLE df_gs25_oneplusone as SELECT *from gs25.df_gs25_oneplusone ;
CREATE TABLE df_gs25_twoplusone as SELECT *from gs25.df_gs25_twoplusone ;
CREATE TABLE df_gs25_threeplusone as SELECT *from gs25.df_gs25_dum ;


CREATE TABLE df_seven11_oneplusone as SELECT *from seven11.df_seven11_oneplusone ;
CREATE TABLE df_seven11_twoplusone as SELECT *from seven11.df_seven11_twoplusone ;
CREATE TABLE df_seven11_dum as SELECT *from seven11.df_seven11_dum ;
CREATE TABLE df_seven11_discount as SELECT *from seven11.df_seven11_discount ;

