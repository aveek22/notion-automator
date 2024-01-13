include ../../ci/make/root.Makefile

.PHONY:	clean tf-plan tf-apply

help-tf:
	@echo $(git rev-parse --show-toplevel)

tf-plan:
	- cd terraform && terraform init && terraform plan
# - terraform plan

tf-apply:
	- cd terraform && terraform apply -auto-approve