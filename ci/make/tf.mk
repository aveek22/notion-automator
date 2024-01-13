include root.mk

.PHONY:	clean tf-plan tf-apply

tf-plan:
	- terraform plan

tf-apply:
	- terraform apply -auto-approve