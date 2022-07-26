<template>
    <div class="pt-5">
        <form @submit.prevent="update" method="post">
            <div class="form-group">
                <label for="nombre">Nombre</label>
                <input
                    type="text"
                    class="form-control"
                    id="nombre"
                    v-model="propietario.nombre"
                    v-validate="'required'"
                    name="nombre"
                    placeholder="Ingrese nombre"
                    :class="{'is-invalid': errors.has('propietario.nombre') && submitted}">
                <div class="invalid-feedback">
                    Please provide a valid name.
                </div>
            </div>
            <div class="form-group">
                <label for="apellido">Apellido</label>
                <textarea
                    name="apellido"
                    class="form-control"
                    id="apellido"
                    v-validate="'required'"
                    v-model="propietario.apellido"
                    :class="{'is-invalid': errors.has('propietario.apellido') && submitted}">
                  </textarea>
                <div class="invalid-feedback">
                    Please provide a valid description.
                </div>
            </div>
            <div class="form-group">
                <label for="edad">Edad</label>
                <textarea
                    name="edad"
                    class="form-control"
                    id="edad"
                    v-validate="'required'"
                    v-model="propietario.edad"
                    :class="{'is-invalid': errors.has('propietario.edad') && submitted}">
                  </textarea>
                <div class="invalid-feedback">
                    Please provide a valid description.
                </div>
            </div>
            <div class="form-group">
                <label for="nacionalidad">Nacionalidad</label>
                <textarea
                    name="nacionalidad"
                    class="form-control"
                    id="nacionalidad"
                    v-validate="'required'"
                    v-model="propietario.nacionalidad"
                    :class="{'is-invalid': errors.has('propietario.nacionalidad') && submitted}">
                  </textarea>
                <div class="invalid-feedback">
                    Please provide a valid description.
                </div>
            </div>
            <button type="submit" class="btn btn-primary">Submit</button>
        </form>
    </div>
</template>
<script>
import axios from 'axios';

export default {
    data() {
        return {
            propietario: {
                nombre: '',
                apellido: '',
                edad: '',
                nacionalidad: '',
                url: '',
            },
            submitted: false
        }
    },
    mounted() {
        axios.get('http://127.0.0.1:8000/api/propietarios/' + this.$route.params.id + '/')
            .then( response => {
                console.log(response.data)
                this.propietario = response.data
            });
    },
    methods: {
        update: function (e) {
            this.$validator.validate().then(result => {
                this.submitted = true;
                if (!result) {
                    return;
                }
                axios.put(`http://127.0.0.1:8000/api/propietarios/${this.propietario.id}/`,
                        this.propietario
                    )
                    .then(response => {
                        this.$router.push('/');
                    })
            });
        }
    },
}
</script>
