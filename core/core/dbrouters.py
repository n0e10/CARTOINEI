class DefaultRouter(object):
    def allow_migrate(self, db, app_label, model_name=None, **hints):
        return db == 'default'


class ActualizacionCartograficaRouter(object):
    def db_for_read(self, model, **hints):
        """ Todas las lecturas del app core se hacen a la conexion actualization
        """
        if model._meta.app_label == 'actualization':
            return 'actualization'
        return None
