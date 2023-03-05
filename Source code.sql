
select * into tablenew from finalfile_sql
where diag_1_desc = 'Diabetes' or diag_2_desc = 'Diabetes' or diag_3_desc = 'Diabetes'

select * from tablenew


ALTER TABLE tablenew
DROP COLUMN [num_lab_procedures]
ALTER TABLE tablenew
DROP COLUMN [num_procedures]
ALTER TABLE tablenew
DROP COLUMN [number_outpatient]
ALTER TABLE tablenew
DROP COLUMN [number_emergency]
ALTER TABLE tablenew
DROP COLUMN [number_inpatient]
ALTER TABLE tablenew
DROP COLUMN [number_diagnoses]
ALTER TABLE tablenew
DROP COLUMN  [metformin]
 ALTER TABLE tablenew
      DROP COLUMN [repaglinide]
	   ALTER TABLE tablenew
      DROP COLUMN [nateglinide]
	   ALTER TABLE tablenew
      DROP COLUMN [chlorpropamide]
	   ALTER TABLE tablenew
      DROP COLUMN [glimepiride]
	   ALTER TABLE tablenew
      DROP COLUMN [acetohexamide]
	   ALTER TABLE tablenew
      DROP COLUMN [glipizide]
	   ALTER TABLE tablenew
      DROP COLUMN [glyburide]
	   ALTER TABLE tablenew
      DROP COLUMN [tolbutamide]
	   ALTER TABLE tablenew
      DROP COLUMN [pioglitazone]
	   ALTER TABLE tablenew
      DROP COLUMN [rosiglitazone]
	   ALTER TABLE tablenew
      DROP COLUMN [acarbose]
	   ALTER TABLE tablenew
      DROP COLUMN [miglitol]
	   ALTER TABLE tablenew
      DROP COLUMN [troglitazone]
	   ALTER TABLE tablenew
      DROP COLUMN [tolazamide]
	   ALTER TABLE tablenew
      DROP COLUMN [examide]
	   ALTER TABLE tablenew
      DROP COLUMN [citoglipton]

 select top 10 * from tablenew

Alter table tablenew
add [Is_Circulatory] numeric

  select top 10 * from tablenew

  UPDATE tablenew
  SET Is_Diabetic = 1

  Update tablenew
  Set Is_Circulatory = 1 where diag_1_desc = 'Circulatory' or diag_2_desc = 'Circulatory' or diag_3_desc = 'Circulatory'

  Update tablenew
  Set Is_Circulatory = 0 where is_circulatory like Null




------Split data into training and testing 
select * 
into #pp
from (
select distinct column1
from [dbo].tablenew) a
order by newid()


select top 70 percent * 
into #train_pp
from #pp


select * 
into [dbo].training
from [dbo].tablenew
where column1 in (select * from #train_pp)


select * 
into [dbo].testing
from [dbo].tablenew
where column1 not in (select * from #train_pp)

select count(*) from testing
select count(*) from training





 