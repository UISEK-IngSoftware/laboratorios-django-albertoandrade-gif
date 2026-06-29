from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand, CommandError
from oauth2_provider.models import Application


class Command(BaseCommand):
    help = "Crea o actualiza el cliente OAuth2 de tipo password para el laboratorio."

    def add_arguments(self, parser):
        parser.add_argument("--username", default="admin")
        parser.add_argument("--client-id", required=True)
        parser.add_argument("--client-secret", required=True)
        parser.add_argument("--name", default="Pokedex React Client")

    def handle(self, *args, **options):
        User = get_user_model()

        try:
            user = User.objects.get(username=options["username"])
        except User.DoesNotExist as exc:
            raise CommandError(
                f'No existe el usuario "{options["username"]}". '
                "Créalo primero con python manage.py createsuperuser."
            ) from exc

        application, created = Application.objects.update_or_create(
            client_id=options["client_id"],
            defaults={
                "user": user,
                "client_type": Application.CLIENT_CONFIDENTIAL,
                "authorization_grant_type": Application.GRANT_PASSWORD,
                "client_secret": options["client_secret"],
                "name": options["name"],
                "skip_authorization": True,
                "allowed_origins": "http://localhost:5173 http://127.0.0.1:5173",
            },
        )

        action = "creado" if created else "actualizado"
        self.stdout.write(
            self.style.SUCCESS(
                f"Cliente OAuth2 {action}: {application.client_id}"
            )
        )
