import boto3
aws_mg_con=boto3.session.Session(profile_name='root')
iam_con=aws_mg_con.resource('iam')
#tüm kayırlı kullanıcıları listeler
for each_users in iam_con.users.all():
	print(each_users.name)

