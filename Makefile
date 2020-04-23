.PHONY: build
build:
	docker build -t a1-301 .
	docker run -d --name a1-301-container -p 80:80 a1-301:latest


.PHONY: start
start:
	docker start a1-301-container


.PHONY: stop
stop:
	docker stop a1-301-container


.PHONY: remove
remove:
	docker rm a1-301-container


.PHONY: reload
reload: stop remove build start


.PHONY: heroku-push
heroku-push: 
	heroku container:push web --app csc301-nagraha3-perei345-a1


.PHONY: heroku-release
heroku-release: 
	heroku container:release web --app csc301-nagraha3-perei345-a1


.PHONY: deploy
deploy: heroku-push heroku-release