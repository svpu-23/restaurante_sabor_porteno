APPS_NEGOCIO = {"restaurante"}

class NegocioRouter:
    def db_for_read(self, model, **hints):
        return "negocio" if model._meta.app_label in APPS_NEGOCIO else "default"

    def db_for_write(self, model, **hints):
        return "negocio" if model._meta.app_label in APPS_NEGOCIO else "default"

    def allow_relation(self, obj1, obj2, **hints):
        return self.db_for_read(type(obj1)) == self.db_for_read(type(obj2))

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if db == "negocio":
            return False
        return app_label not in APPS_NEGOCIO